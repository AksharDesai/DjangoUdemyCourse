const container = document.querySelector('.container')
let isEditMode = false
let currnetMovieId = null

const deleteBtns = document.querySelectorAll('.delete-btn')
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//<====================== ADD movie Code  ======================>
document.getElementById('MovieForm').addEventListener('submit', async (e) => {
    e.preventDefault()
    const form = e.target;
    const formData = {
        name: document.getElementById('id_name').value,
        rating: document.getElementById('id_rating').value,
      
    };
    console.log("inside the add movie forml listener",currnetMovieId,isEditMode)
    
    const methodd= isEditMode?'PUT':'POST';
    const url= isEditMode?`/movies/${currnetMovieId}/`:'/movies/';

    try {

        const response = await fetch(url, {
            method: methodd,
            body: JSON.stringify(formData) ,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest'
            }
        })

        const data = await response.json();

        console.log(data)
        if (data) {
            
            if (isEditMode) {
                // Update existing movie card
                const movieCard = document.querySelector(`button[value="${currnetMovieId}"]`).closest('.movie_card');
                movieCard.querySelector('h2').textContent = data.name;
                const form = document.getElementById('MovieForm')
                form.reset();
                isEditMode = false;
                currnetMovieId = null;
                submitBtn.textContent = 'Add Movie';
                cancelBtn.style.display = 'none';
                document.getElementById('movie_id').value = '';
                clearErrors();
            }else{
                
                
                movie = `
                <div class="movie_card">
                <h2>${data.name} </h2> 
                <button class="delete-btn" name="delete" value="${data.id}">delete</button>
                <button class="edit-btn" name="edit" value="${data.id}" >edit</button>
                </div>
                `
                container.insertAdjacentHTML('afterbegin', movie);
                form.reset()
            }
        }else{
            console.log('response not recived from backend properly');
            
        }
            
            const deleteBtn = document.querySelector('.delete-btn')
            
            deleteBtn.addEventListener('click',async(e)=>{
                const id = e.target.value
                const movieCard = e.target.closest('.movie_card')
                deleteCode(id,movieCard)
            })
            
            
        }
        catch (error) {
            console.log(error)
            alert('failed to add product try again')
        }
})

//<====================== Delete Movie Listener ======================>

deleteBtns.forEach(btn => {
    btn.addEventListener('click',async(e)=>{
        const id = e.target.value
        const movieCard = e.target.closest('.movie_card')
        deleteCode(id,movieCard)
    })

})

//<====================== Delete Movie Code ======================>

async function deleteCode(id,movie_card){
        


    console.log(id)
    
    try{
        const response = await fetch(`/movies/delete/${id}/`,{
            method : 'DELETE',
            headers:{
                'X-CSRFToken':csrfToken,
                'X-Requested-With':'XMLHttpRequest'

            }
        })

        if (response.ok) {

            console.log('delete element code here');
          
            console.log('Movie deleted successfully');
            
            movie_card.remove()

            
        }else{
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    }catch(error){
        console.warn(error)
        alert('Catch:- Failed to Delete Movie ');
    }
    

}

//<====================== Edit Movie Listener ======================>
    
    const editBtns = document.querySelectorAll('.edit-btn')
    const submitBtn = document.getElementById('submitBtn');
    const cancelBtn = document.getElementById('cancelEdit');

    console.log(editBtns);
    
    
    
    editBtns.forEach(btn => {
        console.log(btn);
        
        btn.addEventListener('click',async(e)=>{
            isEditMode = true;
            console.log("button clicked");
            
            currnetMovieId= e.target.value
           
    
            editCode(currnetMovieId)

    
        })
    });


//<====================== Edit Movie Code ======================>

//populate form
async function editCode(currnetMovieId) {

    try{
        //fetch movie data

        const response = await fetch(`/movies/${currnetMovieId}/`)
        const movie = await response.json()

        console.log(movie);
        console.log(movie.name);
        console.log(movie.rating);
        console.log(currnetMovieId);
        
        
        document.getElementById('id_name').value = movie.name
        document.getElementById('id_rating').value = movie.rating
        document.getElementById('movie_id').value = currnetMovieId

        submitBtn.textContent = 'Update'
        cancelBtn.style.display = 'inline-block'

        console.log(isEditMode);
        console.log(currnetMovieId);


        cancelBtn.addEventListener('click', () => {

            const form = document.getElementById('MovieForm')
            form.reset();
             isEditMode = false;
             currnetMovieId = null;
             submitBtn.textContent = 'Add Movie';
             cancelBtn.style.display = 'none';
             document.getElementById('movie_id').value = '';
             clearErrors();
        });
        
    }
    catch(error){
        console.error('Error fetching movie',error);
        
    }
}



function clearErrors() {
    document.querySelectorAll('.error-message').forEach(el => {
        el.textContent = '';
    });
}

