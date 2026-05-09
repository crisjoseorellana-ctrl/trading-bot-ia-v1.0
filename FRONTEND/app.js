async function loadSignal() {

    const response = await fetch(
        "https://onrender.com"
    )

    const data = await response.json()

    const signalElement = document.getElementById("signal")

    signalElement.innerText = data.signal

    signalElement.className = "signal"

    if (data.signal === "BULLISH") {
        signalElement.classList.add("bullish")
    } else {
        signalElement.classList.add("bearish")
    }

    document.getElementById("probability").innerText =
        `Bullish: ${data.bullish_probability}%`

    document.getElementById("rsi").innerText =
        `RSI: ${data.rsi}`
}

loadSignal()

setInterval(loadSignal, 15000)
