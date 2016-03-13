/*Objective: Practice sorting an array.

Resources - Here are some quick tutorials on sort: 
JavaScript Array sort() http://www.w3schools.com/jsref/jsref_sort.asp
Sorting an Array of Objects by Property https://davidwalsh.name/array-sort

Task: An array of objects, librarylibrary, is provided for you in the editor. 
Complete the code below so that it sorts library's elements alphabetically by book name and then prints library.

Note: There is no input to be read, and there are no sample test cases.*/


function sortLibrary() {
    // var library is defined, use it in your code
    // use console.log(library) to output the sorted library data
    
    console.log(library.sort(function(a,b){return a.title > b.title}));
    
    /* the function you pass as a parameter to sort() will be called repeatedly by sort() as it processes the whole array. sort() doesn't know or care about the datatype of the things in the array: each time it needs to know "Does item A come before item B?" it just calls your function. You don't need to worry about what type of sort algorithm is used internally by sort(), indeed one browser might use a different algorithm to another, but that's OK because you just have to provide a way for it to compare any two items from your array.

Your function could have an if / else if / else structure to decide what result to return, but for numbers simply returning (a-b) will achieve this for you because the result of the subtraction will be -ve, 0 or +ve and correctly put the numbers in ascending order. Returning (b-a) would put them descending*/
} 

// tail starts here
var library = [
    {
        author: 'Bill Gates',
        title: 'The Road Ahead',
        libraryID: 1254
    },
    {
        author: 'Steve Jobs',
        title: 'Walter Isaacson',
        libraryID: 4264
    },
    {
        author: 'Suzanne Collins',
        title: 'Mockingjay: The Final Book of The Hunger Games',
        libraryID: 3245
    }
];

sortLibrary();

