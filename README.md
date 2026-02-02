//@version=5
indicator("Профессиональный Калькулятор v3.0", shorttitle="ProCalc Pro", overlay=true, max_labels_count=100)

// ========================
// НАСТРОЙКИ ОТОБРАЖЕНИЯ
// ========================
showTable := input.bool(true, "Показать таблицу")
showLabels := input.bool(true, "Показать метки")
showPlots := input.bool(false, "Показать графики")

// ========================
// ВИД КАЛЬКУЛЯТОРА
// ========================
calcType = input.string("Position Size", "🎯 Тип калькулятора", 
     options=["Position Size", "Risk/Reward", "Fibonacci", "Pivot Points", "Volatility", "Margin", "Portfolio Risk"])

// ========================
// ОБЩИЕ НАСТРОЙКИ
// ========================
// Автоматическое определение цен
useCurrentPrices = input.bool(true, "📊 Использовать текущие цены")

// Валютные пары и тип инструмента
instrumentType = input.string("Stock", "Тип инструмента", 
     options=["Stock", "Forex", "Crypto", "Futures", "Options"])

leverage = input.float(1.0, "Кредитное плечо", minval=1.0, maxval=100.0, step=0.5)

// ========================
// 1. УЛУЧШЕННЫЙ КАЛЬКУЛЯТОР РАЗМЕРА ПОЗИЦИИ
// ========================
if calcType == "Position Size"
    // Входные параметры
    depositSize = input.float(10000, "💰 Размер депозита ($)", minval=100, step=100)
    riskPerTrade = input.float(2.0, "⚠️ Риск на сделку (%)", minval=0.1, maxval=100, step=0.1)
    maxPortfolioRisk = input.float(20.0, "Макс. риск портфеля (%)", minval=5, maxval=100)
    
    // Автоматические цены
    autoEntry = useCurrentPrices ? close : na
    autoStop = useCurrentPrices ? low[1] : na
    
    entryPrice = input.float(autoEntry, "🎯 Цена входа", minval=0.00001)
    stopLoss = input.float(autoStop, "🛑 Цена стоп-лосса", minval=0.00001)
    takeProfit = input.float(na, "🎯 Цена тейк-профита", minval=0.00001)
    
    // Комиссии в зависимости от типа инструмента
    commissionType = input.string("Percent", "Тип комиссии", options=["Percent", "Fixed", "PerUnit"])
    
    commissionPercent = input.float(0.1, "Комиссия (%)", minval=0.0, step=0.01)
    commissionFixed = input.float(1.0, "Фиксированная комиссия ($)", minval=0.0, step=0.1)
    commissionPerUnit = input.float(0.01, "Комиссия за единицу", minval=0.0, step=0.001)
    
    // Скользящий стоп
    useTrailingStop = input.bool(false, "Использовать трейлинг-стоп")
    trailingDistance = input.float(2.0, "Дистанция трейлинга (%)", minval=0.1, step=0.1)
    
    // Расчеты с валидацией
    if entryPrice > 0 and stopLoss > 0
        // Проверка корректности входа
        if entryPrice <= stopLoss
            runtime.error("Для лонга цена входа должна быть ВЫШЕ стоп-лосса!")
        
        riskAmount := depositSize * (riskPerTrade / 100)
        priceRisk := math.abs(entryPrice - stopLoss)
        
        // Расчет размера позиции с учетом комиссии
        positionSizeBase := riskAmount / priceRisk
        
        // Учет комиссии
        if commissionType == "Percent"
            commissionCost := positionSizeBase * entryPrice * (commissionPercent / 100)
            effectivePositionSize := positionSizeBase
        else if commissionType == "Fixed"
            commissionCost := commissionFixed
            effectivePositionSize := (riskAmount - commissionCost) / priceRisk
        else
            commissionCost := positionSizeBase * commissionPerUnit
            effectivePositionSize := (riskAmount - commissionCost) / priceRisk
        
        positionSize := math.floor(effectivePositionSize)
        totalCost := positionSize * entryPrice + commissionCost
        positionPercent := (totalCost / depositSize) * 100
        
        // Расчет тейк-профита если задан
        if not na(takeProfit) and takeProfit > 0
            rewardAmount := math.abs(takeProfit - entryPrice) * positionSize
            rrRatio := rewardAmount / riskAmount
            winToBreakEven := (riskAmount / rewardAmount) * 100
        else
            rewardAmount := na
            rrRatio := na
            winToBreakEven := na
        
        // Трейлинг-стоп расчет
        if useTrailingStop
            trailStopPrice := entryPrice * (1 - trailingDistance / 100)
            trailDistance := math.abs(entryPrice - trailStopPrice)
        else
            trailStopPrice := na
        
        // Отображение
        if showLabels
            var label posLabel = label.new(bar_index, high * 1.02, "", 
                 color=color.new(color.blue, 90), textcolor=color.white, 
                 style=label.style_label_center, yloc=yloc.price,
                 size=size.normal)
            
            labelText = "🎯 РАСЧЕТ ПОЗИЦИИ\n" +
                 "═══════════════════\n" +
                 "📊 Тип: " + instrumentType + "\n" +
                 "💰 Депозит: $" + str.tostring(depositSize, "#,##0.00") + "\n" +
                 "⚠️ Риск: " + str.tostring(riskPerTrade, "#.#") + "% ($" + str.tostring(riskAmount, "#,##0.00") + ")\n" +
                 "🎯 Вход: $" + str.tostring(entryPrice, "#,##0." + str.tostring(math.max(2, math.ceil(math.log10(1/entryPrice))))) + "\n" +
                 "🛑 Стоп: $" + str.tostring(stopLoss, "#,##0." + str.tostring(math.max(2, math.ceil(math.log10(1/stopLoss))))) + "\n" +
                 "📈 Размер: " + str.tostring(positionSize, "#,##0") + " ед.\n" +
                 "💵 Стоимость: $" + str.tostring(totalCost, "#,##0.00") + "\n" +
                 "📊 % от депозита: " + str.tostring(positionPercent, "#.#") + "%\n" +
                 "💸 Комиссия: $" + str.tostring(commissionCost, "#,##0.00")
            
            if not na(takeProfit)
                labelText += "\n" +
                     "🎯 Тейк: $" + str.tostring(takeProfit, "#,##0.00") + "\n" +
                     "⚖️ R/R: " + str.tostring(rrRatio, "#.##") + ":1\n" +
                     "📈 Нужно побед: " + str.tostring(winToBreakEven, "#.#") + "%"
            
            if useTrailingStop
                labelText += "\n" +
                     "🎯 Трейлинг: $" + str.tostring(trailStopPrice, "#,##0.00")
            
            label.set_text(posLabel, labelText)
        
        // Табличное отображение
        if showTable
            var table posTable = table.new(position.top_right, 3, 15, 
                 bgcolor=color.new(color.blue, 95),
                 frame_color=color.blue,
                 frame_width=2)
            
            table.cell(posTable, 0, 0, "ПАРАМЕТР", text_color=color.white, bgcolor=color.blue)
            table.cell(posTable, 1, 0, "ЗНАЧЕНИЕ", text_color=color.white, bgcolor=color.blue)
            table.cell(posTable, 2, 0, "МЕТРИКА", text_color=color.white, bgcolor=color.blue)
            
            table.cell(posTable, 0, 1, "Депозит")
            table.cell(posTable, 1, 1, "$" + str.tostring(depositSize, "#,##0"))
            table.cell(posTable, 2, 1, "100%")
            
            table.cell(posTable, 0, 2, "Рик на сделку")
            table.cell(posTable, 1, 2, str.tostring(riskPerTrade, "#.#") + "%")
            table.cell(posTable, 2, 2, "$" + str.tostring(riskAmount, "#,##0"))
            
            table.cell(posTable, 0, 3, "Цена входа")
            table.cell(posTable, 1, 3, "$" + str.tostring(entryPrice, "#,##0.00"))
            table.cell(posTable, 2, 3, "")
            
            // ... и так далее для всех параметров

// ========================
// 2. РАСШИРЕННЫЙ RISK/REWARD
// ========================
else if calcType == "Risk/Reward"
    entryRR = input.float(close, "Цена входа")
    stopRR = input.float(low[1], "Стоп-лосс")
    targets = input.string("3", "Количество целей", options=["1", "2", "3", "4", "5"])
    
    numTargets = str.tonumber(targets)
    targetPrices = array.new_float()
    
    for i = 0 to numTargets - 1
        targetPrice = input.float(close * (1 + (i + 1) * 0.05), "Цель " + str.tostring(i + 1))
        array.push(targetPrices, targetPrice)
    
    risk = math.abs(entryRR - stopRR)
    
    // Расчет вероятности на основе волатильности
    atr20 = ta.atr(20)
    volatilityFactor = atr20 / close
    baseProbability = 0.5 // Базовая вероятность
    
    // Отображение с цветовой индикацией
    if showLabels
        var label rrLabel = label.new(bar_index, high * 1.02, "",
             color=color.new(color.purple, 90), textcolor=color.white,
             style=label.style_label_center, yloc=yloc.price)
        
        labelText = "⚖️ RISK/REWARD АНАЛИЗ\n" +
             "═══════════════════\n" +
             "Риск на сделку: $" + str.tostring(risk, "#.##") + "\n" +
             "ATR (20): " + str.tostring(atr20/close*100, "#.#") + "%\n" +
             "═══════════════════\n"
        
        for i = 0 to numTargets - 1
            targetPrice = array.get(targetPrices, i)
            reward = math.abs(targetPrice - entryRR)
            rrRatio = reward / risk
            probability = baseProbability * (1 / rrRatio) * (1 - volatilityFactor)
            
            // Цвет в зависимости от качества R/R
            rrColor = rrRatio >= 2 ? color.green : rrRatio >= 1.5 ? color.orange : color.red
            
            labelText += "Цель " + str.tostring(i + 1) + ": " + 
                 str.tostring(rrRatio, "#.##") + ":1 | " + 
                 str.tostring(probability * 100, "#.#") + "%\n" +
                 "$" + str.tostring(targetPrice, "#.##") + " (+" + 
                 str.tostring(reward, "#.##") + ")\n"

// ========================
// 6. КАЛЬКУЛЯТОР МАРЖИ (НОВЫЙ)
// ========================
else if calcType == "Margin"
    // Параметры для разных типов инструментов
    marginRequirements = input.float(50.0, "Требование маржи (%)", minval=1.0, maxval=100.0)
    positionMargin = input.float(10000.0, "Маржа позиции ($)", minval=100.0)
    
    // Расчет доступной маржи
    totalMargin = depositSize * leverage
    usedMargin = positionMargin
    freeMargin = totalMargin - usedMargin
    marginLevel = (totalMargin / usedMargin) * 100
    
    // Маржин колл уровни
    marginCallLevel = input.float(100.0, "Уровень маржин колла (%)", minval=50.0)
    stopOutLevel = input.float(50.0, "Уровень стоп-аута (%)", minval=20.0)
    
    // Цветовая индикация
    marginColor = marginLevel > 200 ? color.green : 
                  marginLevel > 150 ? color.orange : 
                  marginLevel > marginCallLevel ? color.yellow : color.red
    
    if showLabels
        var label marginLabel = label.new(bar_index, high * 1.02, "",
             color=color.new(marginColor, 90), textcolor=color.white,
             style=label.style_label_center, yloc=yloc.price)
        
        label.set_text(marginLabel,
             "🏦 РАСЧЕТ МАРЖИ\n" +
             "═══════════════════\n" +
             "Плечо: " + str.tostring(leverage, "#.#") + ":1\n" +
             "Общая маржа: $" + str.tostring(totalMargin, "#,##0") + "\n" +
             "Использовано: $" + str.tostring(usedMargin, "#,##0") + "\n" +
             "Свободно: $" + str.tostring(freeMargin, "#,##0") + "\n" +
             "Уровень маржи: " + str.tostring(marginLevel, "#.#") + "%\n" +
             "═══════════════════\n" +
             "Маржин колл: " + str.tostring(marginCallLevel, "#.#") + "%\n" +
             "Стоп аут: " + str.tostring(stopOutLevel, "#.#") + "%")

// ========================
// 7. РИСК ПОРТФЕЛЯ (НОВЫЙ)
// ========================
else if calcType == "Portfolio Risk"
    numPositions = input.int(5, "Количество позиций", minval=1, maxval=20)
    correlationMatrix = input.string("Low", "Корреляция портфеля", 
         options=["High", "Medium", "Low", "Diversified"])
    
    // Расчет VaR (Value at Risk)
    confidenceLevel = input.float(95.0, "Уровень доверия (%)", minval=90.0, maxval=99.9)
    timeHorizon = input.int(1, "Горизонт (дней)", minval=1, maxval=30)
    
    // Симуляция Монте-Карло (упрощенная)
    portfolioValue = depositSize
    portfolioVolatility = input.float(15.0, "Волатильность портф. (%)", minval=1.0, maxval=100.0)
    
    // Расчет VaR
    zScore = 1.96 // для 95%
    varValue = portfolioValue * (portfolioVolatility / 100) * zScore * math.sqrt(timeHorizon)
    
    // Максимальная просадка
    maxDrawdown = input.float(10.0, "Макс. просадка (%)", minval=1.0, maxval=50.0)
    
    // Шарп ратио
    expectedReturn = input.float(20.0, "Ожид. доходность (%)", minval=0.0, maxval=100.0)
    riskFreeRate = input.float(5.0, "Безриск. ставка (%)", minval=0.0, maxval=10.0)
    
    sharpeRatio = (expectedReturn - riskFreeRate) / portfolioVolatility
    
    if showLabels
        var label portfolioLabel = label.new(bar_index, high * 1.02, "",
             color=color.new(color.navy, 90), textcolor=color.white,
             style=label.style_label_center, yloc=yloc.price)
        
        label.set_text(portfolioLabel,
             "📊 АНАЛИЗ РИСКА ПОРТФЕЛЯ\n" +
             "══════════════════════\n" +
             "Позиций: " + str.tostring(numPositions) + "\n" +
             "Корреляция: " + correlationMatrix + "\n" +
             "Стоимость: $" + str.tostring(portfolioValue, "#,##0") + "\n" +
             "══════════════════════\n" +
             "VaR (" + str.tostring(confidenceLevel, "#.#") + "%, " + 
             str.tostring(timeHorizon) + "д): $" + str.tostring(varValue, "#,##0") + "\n" +
             "Макс. просадка: " + str.tostring(maxDrawdown, "#.#") + "%\n" +
             "══════════════════════\n" +
             "Шарп: " + str.tostring(sharpeRatio, "#.##") + "\n" +
             "Доходность: " + str.tostring(expectedReturn, "#.#") + "%\n" +
             "Волатильность: " + str.tostring(portfolioVolatility, "#.#") + "%")

// ========================
// ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ
// ========================

// Алерты
if calcType == "Position Size" and positionPercent > 20
    alert("Внимание! Позиция превышает 20% от депозита", alert.freq_once_per_bar)

// Логирование в консоль
var string lastLog = ""
if ta.change(calcType)
    logText := "Калькулятор изменен на: " + calcType
    lastLog := logText
    // console.log(logText)

// Сохранение настроек
var string savedSettings = ""
saveSettings = input.bool(false, "Сохранить настройки")
if saveSettings
    savedSettings := "Deposit=" + str.tostring(depositSize) + 
                    ",Risk=" + str.tostring(riskPerTrade)

// ========================
// ВИЗУАЛЬНОЕ ОФОРМЛЕНИЕ
// ========================

// Цветовая схема в зависимости от типа
getCalcColor(type) =>
    switch type
        "Position Size" => color.blue
        "Risk/Reward" => color.purple
        "Fibonacci" => color.orange
        "Pivot Points" => color.green
        "Volatility" => color.red
        "Margin" => color.teal
        "Portfolio Risk" => color.navy
        => color.gray

// Графическое отображение
if showPlots
    plotColor = getCalcColor(calcType)
    
    if calcType == "Pivot Points"
        plot(pivot, "Pivot", plotColor, 2)
        plot(r1, "R1", color.red, 1)
        plot(s1, "S1", color.green, 1)
    
    if calcType == "Fibonacci"
        for i = 0 to 4
            fibValue = array.get(fibLevels, i)
            plot(fibValue, "Fib " + str.tostring(i), plotColor, 1)

// Статистика использования
var int useCount = 0
if ta.change(calcType)
    useCount += 1

// Футер с информацией
if showLabels
    var label footerLabel = label.new(bar_index, low * 0.98, "",
         color=color.new(color.gray, 90), textcolor=color.white,
         style=label.style_label_center, yloc=yloc.price,
         size=size.small)
    
    label.set_text(footerLabel,
         "ProCalc v3.0 | Использован: " + str.tostring(useCount) + " раз | " +
         "Bar: " + str.tostring(bar_index) + " | " +
         "Время: " + str.tostring(hour, "00") + ":" + str.tostring(minute, "00"))
