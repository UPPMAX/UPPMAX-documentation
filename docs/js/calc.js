// note to self: launch http server serving current dir with
// `python3 -m http.server`
// (can't load `prices.json` if you open the html directly in a browser)
var prices;
var current_prices; // = prices["pelle"];

async function loadPrices() {
	const response = await fetch("../js/prices.json");
	await response.json().then((p) => {
		prices = p;
		current_prices = prices["pelle"];
	});
}


var find = (sel) => {
	let r = document.querySelectorAll(sel);
	let first = Array.from(sel)[0];

	// if looking up id, assume unique
	if (first == "#") {
		return r[0];
	} else {
		return r;
	}
};

let current_values = {
	"cpu": 0,
	"cpu-highmem": 0,
	"gpu-small": 0,
	"gpu-medium": 0,
	"gpu-large": 0,
	"proj-storage": 0,
};

function changeService(event) {
	current_prices = prices[event.srcElement.value];
	updateAllTheThings();
}

function updateAllTheThings() {
	var sum = 0;

	for (let resource in current_prices) {
		let price_info = current_prices[resource];

		let input = find("#" + resource);
		let tr = input.parentNode.parentNode;

		input.value = current_values[resource]; //price_info.value;

		input.dataset.price = price_info.price;
		input.dataset.multiplier = price_info.multiplier;

		tr.querySelector(".input-unit").textContent = price_info.input_unit;
		tr.querySelector(".price").textContent = price_info.price.toFixed(2) + " " + price_info.price_unit;

		let total = current_values[resource] * price_info.multiplier * price_info.price
		sum += total;

		tr.querySelector(".total").textContent = total.toLocaleString("sv-SE");
	}

	let price_sum = find("#price-sum");
	price_sum.textContent = sum.toLocaleString("sv-SE");
}

function updateSum() {
	let price_sum = find("#price-sum");
	let sum = 0;

	for (let resource in current_prices) {
		sum += current_values[resource] * current_prices[resource].multiplier * current_prices[resource].price;
	}

	price_sum.textContent = sum.toLocaleString("sv-SE");
}

function updateCost(event) {
	let input = event.srcElement;
	let resource = input.id;

	let amount = input.valueAsNumber;
	let price = Number(input.dataset.price);
	let multiplier = Number(input.dataset.multiplier);

	// NaN
	if (amount !== amount) {
		amount = 0;
	} else if (price !== price) {
		console.log("price is NaN??");
		return;
	}

	current_values[resource] = amount;

	// find the thingy marked with the `total` class within the current row
	let tr = input.parentNode.parentNode;
	let total = tr.querySelector(".total");

	total.textContent = (amount * multiplier * price).toLocaleString("sv-SE");

	updateSum();
}


document.addEventListener("DOMContentLoaded", () => {
	document.getElementsByName("service").forEach((s) => {
		s.addEventListener("input", changeService);
	});

	document.querySelectorAll("#ucalc input").forEach((i) => {
		i.addEventListener("input", updateCost);
	});

	// update all the things once the prices are loaded
	loadPrices().then(updateAllTheThings);
});
