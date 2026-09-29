"""Simplified STEP models for AGD6 parts without library 3D models (KiCad coords: model Y = -footprint Y, Z up)."""
from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCP.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCP.XCAFApp import XCAFApp_Application
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ColorSurf
from OCP.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCP.STEPCAFControl import STEPCAFControl_Writer
from OCP.STEPControl import STEPControl_AsIs
from OCP.Interface import Interface_Static
OUT = ""  # output directory (cwd by default)

def box(x0, x1, y0, y1, z0, z1):
    # footprint coords (y down) -> model coords (y up)
    return BRepPrimAPI_MakeBox(gp_Pnt(x0, -y1, z0), gp_Pnt(x1, -y0, z1)).Shape()

def pin(x, y, d, z0, z1):
    return BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(x, -y, z0), gp_Dir(0, 0, 1)), d / 2, z1 - z0).Shape()

def write(name, parts):
    app = XCAFApp_Application.GetApplication_s()
    doc = TDocStd_Document(TCollection_ExtendedString("MDTV-XCAF"))
    app.InitDocument(doc)
    st = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    ct = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    for shape, rgb in parts:
        lab = st.AddShape(shape, False)
        ct.SetColor(lab, Quantity_Color(*rgb, Quantity_TOC_RGB), XCAFDoc_ColorSurf)
    Interface_Static.SetCVal_s("write.step.unit", "MM")
    w = STEPCAFControl_Writer()
    w.Transfer(doc, STEPControl_AsIs)
    assert w.Write(OUT + name) == 1
    print("wrote", name)

YEL, BLK, BRASS, GRY = (0.95, 0.8, 0.1), (0.12, 0.12, 0.12), (0.8, 0.65, 0.3), (0.55, 0.55, 0.55)

# AMASS XT30PW horizontal (simplified envelope from the KiCad footprint fab outline; housing 10.2 x 5.2 mm)
def xt30(name, pads, pegs, fab):
    x0, x1, y0, y1 = fab
    cx = (pads[0] + pads[1]) / 2
    parts = [(box(x0, x1, y0 + 9.0, y1, 0, 1.6), YEL),                        # base with mounting ears
             (box(cx - 5.1, cx + 5.1, y0, y1, 0, 5.2), YEL)]                   # plug housing, mating face at y0
    parts += [(pin(x, 0, 1.9, -3.0, 0.5), BRASS) for x in pads]
    parts += [(pin(x, y, 1.0, -2.5, 0.5), YEL) for x, y in pegs]
    write(name, parts)

# text engraving helper (module markings)
from OCP.StdPrs import StdPrs_BRepFont, StdPrs_BRepTextBuilder
from OCP.NCollection import NCollection_Utf8String
from OCP.gp import gp_Ax3, gp_Vec
from OCP.Graphic3d import Graphic3d_HTA_CENTER, Graphic3d_VTA_CENTER
from OCP.BRepPrimAPI import BRepPrimAPI_MakePrism
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def text(t, size, x, y, z, h=0.06):
    f = StdPrs_BRepFont()
    assert f.Init(NCollection_Utf8String(FONT), size, 0)
    face = StdPrs_BRepTextBuilder().Perform(f, NCollection_Utf8String(t), gp_Ax3(gp_Pnt(x, -y, z), gp_Dir(0, 0, 1)),
                                            Graphic3d_HTA_CENTER, Graphic3d_VTA_CENTER)
    return BRepPrimAPI_MakePrism(face, gp_Vec(0, 0, h)).Shape()



def main():
    xt30("AMASS_XT30PW-M_Horizontal_AGD6.step", (0, -5), [(-8, -10), (3, -10)], (-9.65, 4.65, -13.6, 2.25))
    xt30("AMASS_XT30PW-F_Horizontal_AGD6.step", (0, 5), [(-3, -5), (8, -5)], (-4.65, 9.65, -14.55, 2.25))

    WHITE = (0.95, 0.95, 0.95)

    # TRACO THL 40WI: 1" x 1" x 0.4" case (KiCad footprint F.Fab outline), pins d1.0 (CHECK_DATASHEET height)
    TOPT = 10.7
    parts = [(box(-10.95, 15.95, -3.72, 23.65, 0.5, TOPT), BLK)]
    parts += [(pin(x, y, 1.0, -3.5, 0.5), BRASS) for x, y in ((0, 0), (5.08, 0), (12.7, 0), (-7.62, 20.32), (2.54, 20.32), (12.7, 20.32))]
    cx, cy = 2.5, 9.965
    parts += [(text("TRACO POWER", 2.6, cx, cy - 5.0, TOPT), WHITE),
              (text("THL 40-4812WI", 3.0, cx, cy, TOPT), WHITE),
              (text("18-75V  12V 3.35A", 1.8, cx, cy + 4.5, TOPT), WHITE),
              (pin(-9.0, -1.8, 1.2, TOPT, TOPT + 0.06), WHITE)]
    write("TRACO_THL40WI_AGD6.step", parts)

    # Generic SMD bodies for library footprints whose 3D model is absent in KiCad 10.0.6 (XY = F.Fab outline, height = typical, CHECK_DATASHEET)
    import json, os
    bb = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fab_bb.json")))
    bb.setdefault("VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm", ["F.Fab", -1.5, 1.5, -1.5, 1.5])
    H = {"Fuse_Littelfuse-NANO2-451_453": (2.69, (0.9, 0.9, 0.85)), "Fuse_1812_4532Metric": (1.6, (0.85, 0.8, 0.6)),
         "L_Bourns_SRP1245A": (4.5, (0.25, 0.25, 0.25)), "L_CommonMode_Wurth_WE-CNSW-1206": (1.8, (0.3, 0.3, 0.3)),
         "Infineon_PG-DSO-8-43": (1.75, BLK), "Sensirion_DFN-4_1.5x1.5mm_P0.8mm_SHT4x_NoCentralPad": (0.5, GRY),
         "VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm": (0.9, BLK)}
    for name, (h, col) in H.items():
        _, x0, x1, y0, y1 = bb[name]
        write(name + "_AGD6.step", [(box(x0, x1, y0, y1, 0, h), col)])


if __name__ == "__main__":
    main()
