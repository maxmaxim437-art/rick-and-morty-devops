const charactersContainer =
    document.getElementById("characters-container");

const searchInput =
    document.getElementById("search-input");

const locationFilter =
    document.getElementById("location-filter");

const resultsCount =
    document.getElementById("results-count");

const statusIndicator =
    document.getElementById("status-indicator");

const statusText =
    document.getElementById("status-text");


let characters = [];


// Load characters from Flask API

async function loadCharacters() {

    try {
        const response = await fetch("/characters");

        if (!response.ok) {
            throw new Error("Failed to load characters");
        }

        characters = await response.json();

        populateLocationFilter();
        displayCharacters(characters);

    } catch (error) {
        charactersContainer.textContent =
            "Unable to load characters.";

        resultsCount.textContent = "Error loading data";
    }
}


// Create location filter options

function populateLocationFilter() {

    const locations = [
        ...new Set(characters.map(character => character.Location))
    ].filter(Boolean).sort();

    locations.forEach(location => {

        const option = document.createElement("option");

        option.value = location;
        option.textContent = location;

        locationFilter.appendChild(option);
    });
}


// Display character cards

function displayCharacters(data) {

    charactersContainer.replaceChildren();

    resultsCount.textContent =
        `${data.length} characters found`;

    if (data.length === 0) {
        const message = document.createElement("p");
        message.className = "message";
        message.textContent = "No characters found.";

        charactersContainer.appendChild(message);
        return;
    }

    data.forEach(character => {

        const card = document.createElement("article");
        card.className = "character-card";

        const image = document.createElement("img");
        image.src = character.Image;
        image.alt = character.Name;
        image.loading = "lazy";

        const info = document.createElement("div");
        info.className = "character-info";

        const name = document.createElement("h3");
        name.textContent = character.Name;

        const location = document.createElement("p");
        location.textContent = `Location: ${character.Location}`;

        info.append(name, location);
        card.append(image, info);

        charactersContainer.appendChild(card);
    });
}


// Search and filter characters

function filterCharacters() {

    const searchValue = searchInput.value.toLowerCase();
    const selectedLocation = locationFilter.value;

    const filteredCharacters = characters.filter(character => {

        const matchesName =
            character.Name.toLowerCase().includes(searchValue);

        const matchesLocation =
            selectedLocation === "" ||
            character.Location === selectedLocation;

        return matchesName && matchesLocation;
    });

    displayCharacters(filteredCharacters);
}


// Check server health

async function checkServerHealth() {

    try {
        const response = await fetch("/healthcheck");

        if (!response.ok) {
            throw new Error("Server unavailable");
        }

        const data = await response.json();

        const isHealthy = data.status === "healthy";

        statusIndicator.className =
            isHealthy ? "status-dot online" : "status-dot offline";

        statusText.textContent =
            isHealthy ? "API Online" : "API Unhealthy";

    } catch (error) {

        statusIndicator.className = "status-dot offline";
        statusText.textContent = "API Offline";
    }
}


// Event listeners

searchInput.addEventListener("input", filterCharacters);

locationFilter.addEventListener("change", filterCharacters);


// Start application

loadCharacters();

checkServerHealth();

setInterval(checkServerHealth, 10000);
