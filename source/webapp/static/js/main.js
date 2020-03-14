 <script>
        $('#search_name').keyup(function () {
            $.ajax({
                type: 'GET',
                url: '/accounts/user/ajax/search/',
                data: {
                    q: $('input[id=search_name]').val()
                },
                success: searchSuccess});
            function searchSuccess(data, textStatus, jqXHR)
                {
                    $('#search_results').html(data)
                }
        });
         $("#id_in_first_name").click(function(){
            let search = $("#id_in_first_name:checkbox:checked").length > 0;
            if(search == true){
                console.log($('#search_name'))
                $('#search_name').show()}
            else{
                $('#search_name').hide()}
         });
         $('#id_text').val('').change();
         $('#id_in_first_name').removeAttr("checked")
         </script>
