import yfinance as yf
import pandas as pd
import ta

def get_signal(symbol: str):
    # Descargamos los datos y nos aseguramos de que sean simples (.squeeze())
    df = yf.download(symbol, period="1d", interval="15m")
    
    if df.empty:
        return {"error": "No hay datos para este símbolo"}

    # Fix para el error 1-dimensional: usamos .squeeze() o seleccionamos la columna directamente
    close_prices = df['Close'].squeeze()

    # Cálculo de indicadores
    rsi_series = ta.momentum.RSIIndicator(close_prices).rsi()
    ema_fast_series = ta.trend.EMAIndicator(close_prices, window=9).ema_indicator()
    ema_slow_series = ta.trend.EMAIndicator(close_prices, window=21).ema_indicator()

    # Tomamos el último valor de cada uno
    rsi = float(rsi_series.iloc[-1])
    ema_fast = float(ema_fast_series.iloc[-1])
    ema_slow = float(ema_slow_series.iloc[-1])

    # Tu lógica de probabilidad
    bullish_score = 0
    if rsi > 55: bullish_score += 35
    if ema_fast > ema_slow: bullish_score += 35
    if rsi > 65: bullish_score += 15
    
    return {
        "symbol": symbol,
        "rsi": round(rsi, 2),
        "bullish_probability": bullish_score,
        "signal": "COMPRA" if bullish_score >= 50 else "ESPERAR"
    }