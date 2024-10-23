// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// bullet

//@version=5
indicator("Purple Cloud [ATP]",overlay=true, timeframe="", timeframe_gaps=true)

atrPeriod = input(10, "Supertrend ATR Length")
factor = input.float(3.0, "Supertrend Factor", step = 0.01)

[supertrend, direction] = ta.supertrend(factor, atrPeriod)

x1 = input(40, "Period")
alpha = input.float(0.9, "Alpha", step = 0.1)

x2 = ta.atr(x1) * alpha 
xh = close + x2
xl = close - x2 
a1=ta.vwma(hl2*volume,math.ceil(x1/4))/ta.vwma(volume,math.ceil(x1/4))
a2=ta.vwma(hl2*volume,math.ceil(x1/2))/ta.vwma(volume,math.ceil(x1/2))
a3=2*a1-a2
a4=ta.vwma(a3,x1)

b1 = 0.0
b1 := na(b1[1]) ? ta.sma(close, x1) : (b1[1] * (x1 - 1) + close) / x1

buy  = a4<=xl and close>b1
sell = a4>=xh and close<b1
xs = 0
xs := buy ? 1 : sell ? -1 : xs[1]

barcolor( color = xs==1 ? color.green :xs==-1? color.red:na)

plotshape(buy  and xs != xs[1]  ,  title = "BUY",  text = 'B',  style = shape.labelup,   location = location.belowbar, color= color.green, textcolor = color.white,  size = size.tiny)
plotshape(sell and xs != xs[1] , title = "SELL", text = 'S', style = shape.labeldown, location = location.abovebar, color= color.red,   textcolor = color.white, size = size.tiny)

plotshape(buy  and xs != xs[1] and direction < 0 ,  title = "Strong BUY",  text = '🚀',  style = shape.labelup,   location = location.belowbar, color= color.green, textcolor = color.white,  size = size.tiny)
plotshape(sell and xs != xs[1] and direction > 0 , title = "Strong SELL", text = '☄️', style = shape.labeldown, location = location.abovebar, color= color.red,   textcolor = color.white, size = size.tiny)

ema200=input(false,"Ema 200")
ema50=input(false,"Ema 50")
ema20=input(false,"Ema 20")

plot(ta.ema(close,200),color=ema200?color.black:na,title="Ema 200",linewidth = 4)
plot(ta.ema(close,50),color=ema50?color.blue:na,title="EMA 50",linewidth = 3)
plot(ta.ema(close,20),color=ema20?color.orange:na,title="EMA 20",linewidth = 2)
alertcondition(buy  and xs != xs[1],  "PC Long",  "PC Long")
alertcondition(sell and xs != xs[1], "PC Short", "PC Short")
