import React, {Component } from 'react';
import { getMovies } from '../Service/MoviesService';
import { DeleteItem } from '../Service/MoviesService';

class Movies extends Component {
    state = { 
        movies: getMovies()
     } 
    render() { 
        if(this.state.movies.length ==0 )
            return <p className='ms-3'> there are no movies left </p>
        return (   
            <React.Fragment>
            <p className='ms-3' > there are {this.state.movies.length}  Movies</p>
            <table className="table">
                <thead>
                    <th>Name</th>
                    <th>Id</th>
                    <th>Genre</th>
                    <th>Length</th>
                </thead>
                <tbody>
                {this.state.movies.map(movie=>(
                <tr>
                    <td>{movie.name}</td>
                    <td> {movie.id}</td>
                    <td>{movie.genre}</td>
                    <td>{movie.length}</td>
                    <td> <button className='btn btn-danger' onClick={()=> this.removeItem(movie.id)} > DELETE</button>   </td>
                    <td> <button className='btn btn-danger' onClick={()=> this.updateItem(movie.id)} > PATCH</button>   </td>
                </tr>
                ))}
                </tbody>
            </table>
            </React.Fragment>
        );
    }

    updateItem=(id)=>{
        this.state.movies = this.state.movies.map(movie => {
            if (id===movie.id)
                movie.name='null'
            return movie
        });
        this.setState({movies: this.state.movies});
    }

    removeItem=(id)=>{
    //    this.state.movies = this.state.movies.filter(movie => movie.id !== id );
    //     this.setState({movies: this.state.movies});
        this.setState({movies: DeleteItem(id)})

    }
}
 
export default Movies;
