let movies=[
    {
        id:1,
        name: 'die hard',
        genre: 'Action',
        length: '2:20'
    },
    {
        id:2,
        name: 'die hard2',
        genre: 'Action',
        length: '2:30'
    },
    {
        id:3,
        name: 'fast five',
        genre: 'Action',
        length: '4:20'
    },
    {
        id:4,
        name: 'Taken',
        genre: 'Action',
        length: '1:20'
    },
];


export function getMovies(){
    return movies;
}

export function DeleteItem(id){
    movies= movies.filter(movie => movie.id !==id );
    return movies;
}

export function getMovie(id){
    return movies.find(m => m.id == id);
}