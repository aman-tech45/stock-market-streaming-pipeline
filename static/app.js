async function loadStocks() {

    const response = await fetch("/stocks");

    const stocks = await response.json();

    let html = "";

    for (const symbol in stocks){

        const stock = stocks[symbol];

        html += `
        <div class="card">

            <h2>${symbol}</h2>

            <h3>$${stock.price}</h3>

            <p>🕒 ${stock.timestamp}</p>

        </div>
        `;
    }

    document.getElementById("stocks").innerHTML = html;

}

loadStocks();

setInterval(loadStocks,2000);