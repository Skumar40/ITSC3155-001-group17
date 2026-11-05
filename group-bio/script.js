// Show or hide an individual member's bio.
function toggleBio(bioId) {
    const bio = document.getElementById(bioId);

    if (!bio) return;

    const isHidden = window.getComputedStyle(bio).display === "none";

    bio.style.display = isHidden ? "block" : "none";

    const button = document.querySelector(
        `button[aria-controls="${bioId}"]`
    );

    if (button) {
        button.textContent = isHidden ? "Hide Bio" : "Show Bio";
        button.setAttribute("aria-expanded", String(isHidden));
    }
}

// Switch between Team Bios and Team Vision.
function showSection(sectionId) {
    if (sectionId !== "bios" && sectionId !== "vision") return;

    const biosSection = document.getElementById("bios");
    const visionSection = document.getElementById("vision");

    if (!biosSection || !visionSection) return;

    biosSection.style.display = sectionId === "bios" ? "flex" : "none";
    visionSection.style.display = sectionId === "vision" ? "flex" : "none";
}

// Set the initial accessibility state of each bio button.
document.querySelectorAll("button[aria-controls]").forEach((button) => {
    const bio = document.getElementById(
        button.getAttribute("aria-controls")
    );

    if (bio) {
        const isVisible = window.getComputedStyle(bio).display !== "none";
        button.setAttribute("aria-expanded", String(isVisible));
        button.textContent = isVisible ? "Hide Bio" : "Show Bio";
    }
});
