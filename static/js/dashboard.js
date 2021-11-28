const filterItem = document.querySelector(".genre .filter-wrapper");
const filterImg = document.querySelectorAll(".genre .list-wrapper .list-item");
window.onload = () => { //after window loaded
    filterItem.onclick = (selectedItem) => { //if user click on filterItem div
        if (selectedItem.target.classList.contains("list")) { //if user selected item has .item class
            filterItem.querySelector(".active").classList.remove("active"); //remove the active class which is in first item
            selectedItem.target.classList.add("active"); //add that active class on user selected item
            let filterName = selectedItem.target.getAttribute("data-filter"); //getting data-filter value of user selected item and store in a filtername variable
            filterImg.forEach((image) => {
                let filterImges = image.getAttribute("data-filter"); //getting image data-filter value
                console.log(image)
                //if user selected item data-filter value is equal to images data-filter value
                //or user selected item data-filter value is equal to "all"
                if ((filterImges == filterName) || (filterName == "All")) {
                    image.classList.remove("hide"); //first remove the hide class from the image
                    image.classList.add("show"); //add show class in image
                } else {
                    image.classList.add("hide"); //add hide class in image
                    image.classList.remove("show"); //remove show class from the image
                }
            });
        }
    }
    for (let i = 0; i < filterImg.length; i++) {
        filterImg[i].setAttribute("onclick", ""); //adding onclick attribute in all available images
    }
}