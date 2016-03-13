// explores using for/in loops to iterate over objects in lists, accessing properties of each object using objectname.property
// forEach, string templates
// references: http://stackoverflow.com/questions/1625208/print-content-of-javascript-object
// http://www.w3schools.com/js/js_properties.asp

/*Task

Write a JavaScript program to display the status (i.e. display book name, author name and reading status) of books. You are given an object library in the code's template. It contains a list of books with the above mentioned properties. Your task is to display the following:

If the book is unread:

You still need to read '<book_name>' by <author_name>.
If the book is read:

Already read '<book_name>' by <author_name>.*/

function displayInformation() {
    library.forEach(logItem);
} 

function logItem(book) {
    var template = // string templates
        book.readingStatus ?
        `Already read '${book.title}' by ${book.author}.` :
        `You still need to read '${book.title}' by ${book.author}.`;
    
    console.log(template);
}

// tail starts here
var library = [ 
    {
        title: 'Bill Gates',
        author: 'The Road Ahead',
        readingStatus: true
    },
    {
        title: 'Steve Jobs',
        author: 'Walter Isaacson',
        readingStatus: true
    },
    {
        title: 'Mockingjay: The Final Book of The Hunger Games',
        author: 'Suzanne Collins',
        readingStatus: false
    }
];

displayInformation();
