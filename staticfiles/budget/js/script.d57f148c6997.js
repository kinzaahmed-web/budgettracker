
(function(){

    document.querySelector('#categoryInput').addEventListener("keydown", function(e){
        //if user doesnt enter the enter key
        if(e.which != 13){
            return;
        }
        e.preventDefault()

        var categoryName = this.value
        this.value = ''
        addNewCategory(categoryName)
        updateCategoriesString()
    })

    //add a new category
    function addNewCategory(name){

        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend', 
        `<li class="category">
        <span class="name">${name}</span>
        <span onclick="removeCategory(this)" class="btnRemove bold">X</span>
    </li>`)
    }

})()

//fetch all the categories
function fetchCategoryArray(){
    var categories = []
    document.querySelectorAll('.category').forEach(function(e){
        name = e.querySelector('.name').innerHTML
        if (name == '') return
        //adds that name to the list
        categories.push(name)
    })

    return categories
}

//updates the categories
function updateCategoriesString(){
    categories = fetchCategoryArray()
    document.querySelector('input[name="categoriesString"]').value = categories.join(',')
}

function removeCategory(e){
    e.parentElement.remove()
    updateCategoriesString()
}