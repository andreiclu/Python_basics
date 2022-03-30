// alert('Hello world!');
document.write('Hello World!');
console.log("Hello world");

myName = 'Andrei'

// console.log('Hello '+ myName)

// for (var i=0;i<=100; i++){
//     console.log(i);

// }

// for (var i=50;i<=150;i++){
//     if (i%7===0){
//         console.log(i)
//     }
// }


// var ar= [2,'4','abc',6,false,8,9.11];

// console.log(ar.length);

// console.log(ar);

// ar.push(5);
// console.log(ar)

// ar.pop();
// console.log(ar)


// ar = [0,1];
// fib = [];
// for (var i=2;i<=11;i++) {
//     ar[i]=ar[i-1]+ar[i-2];
//     fib.push(ar[i]);
// }

// console.log(fib)

// function recurisveFib(i = 1){
//     if(i<3) return 1;
//     return recurisveFib(i-1)+recurisveFib(i-2);

// }

function prim(x,y){
    l = [];
    for(var i=x;i<=y;i++){
        var fl = 0;
        for(var j=2;j<i;j++){
            if(i%j==0){
                fl=1;
                break;
            }
        }
        if (i>1 && fl==0){
            console.log(lst.push(i));
        }
    
    }
}

