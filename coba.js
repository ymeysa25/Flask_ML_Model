const sentimen = ['Baik', 'Tidak Baik'];

function findBestValue(arr){
    var hasil = arr[0]
    for(let i = 0; i < arr.length; i++){
        if(hasil  > arr[i]){
            hasil = hasil
        }
        else{
            hasil = arr[i]
        }
    }

    return arr.indexOf(hasil)
}

var nilai = [1,4];
const hasil = "Maka berdasarkan review menunjukan aplikasi tersebut dengan kategori " +  sentimen[findBestValue(nilai)];
console.log(hasil);



