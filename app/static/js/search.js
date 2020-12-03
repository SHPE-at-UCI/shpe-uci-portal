function filterSearch() {
    var input = document.getElementById("alumni_search");

    var filter = input.value.toUpperCase();

    var searchDesc = document.getElementById("searchDescription");

    var ul = document.getElementById("user_results");
    var li = ul.getElementsByTagName("li");

    for (i = 0; i < li.length; i++) {
        var a = li[i].getElementsByTagName("a")[0];
        var txtValue = a.textContent || a.innerText;

        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        }
        else {
            li[i].style.display = "none";
        }
    }
}

