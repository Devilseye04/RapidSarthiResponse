
$("#ph_number").keydown(function(event) {
    k = event.which;

    if ($(this).val().length == 10) {
        if (k == 8) {
            return true;
        } else {
            return false;
        }
    }
});


function validateContact(){
   num = document.getElementById('ph_number').value;
   if(num.length() >10 || num.length<10){
       alert("Please Enter Valid Contact")
   }
}

function cityFilter() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
// }
// function facilityFilter() {
//     var input, filter, table, tr, td, i, txtValue;
//     input = document.getElementById("myInput2");
//     filter = input.value.toUpperCase();
//     table = document.getElementById("myTable");
//     tr = table.getElementsByTagName("tr");
//     for (i = 0; i < tr.length; i++) {
//         td = tr[i].getElementsByTagName("td")[0];
//         if (td) {
//             txtValue = td.textContent || td.innerText;
//             if (txtValue.toUpperCase().indexOf(filter) > -1) {
//                 tr[i].style.display = "";
//             } else {
//                 tr[i].style.display = "none";
//             }
//         }
//     }
// }