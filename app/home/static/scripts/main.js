/*TODO: reformat, restructure javascript code with a main module*/
document.getElementById("container").addEventListener("click", function(e) {
    localStorage.setItem("activeElement", e.target.id);
})
activeCategory = localStorage.getItem("activeElement");

category = document.getElementById(activeCategory);
category.classList.add("active_category");




