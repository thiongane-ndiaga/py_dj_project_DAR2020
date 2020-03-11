(function(){
    document.querySelector("#cate_input").addEventListener('keydown',function(e){
        if(e.keyCode != 13){
            return;
        }
        e.preventDefault();

        var nom_cate = this.value;
        this.value="";
        addCate(nom_cate);
        updCategories();
    })

    function addCate(nom){
        document.querySelector("#cate_group").insertAdjacentHTML('beforeend',
        '<li class="cate_item">'
            +'<span>'+nom+'</span>'
            +'<span class="font-weight-bold text-danger ml-1">x</span>'
        +'</li>'
        )
    }

    function arrayCate(){
        var categories = []
        document.querySelectorAll('')
    }
})()