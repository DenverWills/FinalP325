document.addEventListener("DOMContentLoaded", () => {
    const gallery = document.getElementById("dino-gallery");
    const dinoSelector = document.getElementById("dino-select");
    const showBtn = document.getElementById("show-btn");
    const backBtn = document.getElementById("back-btn");

    let dinoData = [];

    fetch("/api/dinosaurs")
        .then(response => response.json())
        .then(data => {
            dinoData = data;

            // Add 'Show All' option
            const allOption = document.createElement("option");
            allOption.value = "all";
            allOption.textContent = "Show All Dinosaurs";
            dinoSelector.appendChild(allOption);

            // Add individual dino options
            data.forEach(dino => {
                const option = document.createElement("option");
                option.value = dino.image;
                option.textContent = dino.name;
                dinoSelector.appendChild(option);
            });

            showBtn.addEventListener("click", () => {
                gallery.innerHTML = "";

                const selected = dinoSelector.value;

                if (selected === "all") {
                    dinoData.forEach(dino => {
                        const img = document.createElement("img");
                        img.src = dino.image;
                        img.alt = dino.name;
                        img.classList.add("dino-img");
                        gallery.appendChild(img);
                    });
                } else {
                    const img = document.createElement("img");
                    img.src = selected;
                    img.alt = "Selected Dinosaur";
                    img.classList.add("dino-img");
                    gallery.appendChild(img);
                }

                dinoSelector.style.display = "none";
                showBtn.style.display = "none";
                backBtn.style.display = "inline-block";
            });

            backBtn.addEventListener("click", () => {
                gallery.innerHTML = "";
                dinoSelector.style.display = "inline-block";
                showBtn.style.display = "inline-block";
                backBtn.style.display = "none";
                dinoSelector.selectedIndex = 0;
            });
        });
});
