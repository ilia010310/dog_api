## You should build a new API endpoint

---

- That allows an end user to create a new Dog model by making a POST to /api/dogs
- View current dogs that have been saved to the server before by making a GET to /api/dogs, and get, modify, or delete an existing Dog record by making a GET, PUT, or DELETE request (respectively) to /api/dogs/<id> 
- Where <id> is the id of the Dog record to be retrieved, modified, or deleted. Since a Dog includes a foreign key to the breed
- You also need to make the same type of endpoints for dog breed at /api/breeds/ and /api/breeds/<id>.


#### test your endpoints with POSTMAN, taking screenshots of each type of request. There should be 5 requests total for each type of model, for a total of 10 tests and screenshots.

- ##### GET (list), POST to /api/dogs/
- ![GET in dogs](scrinshots/GET_in_dogs.png) <br>
- ![POST in dogs](scrinshots/POST_in_dogs.png) <br>
- ##### GET, PUT, DELETE to /api/dogs/<id>
- ![GET in dogs detail](scrinshots/GET_in_dogs_detail.png) <br>
- ![PUT in dogs detail](scrinshots/PUT_in_dogs_detail.png) <br>
- ![DELETE in dogs detail](scrinshots/DELETE_in_dogs_detail.png) <br>
- ##### GET (list), POST to /api/breeds/
- ![GET_in_breed](scrinshots/GET_in_breed.png) <br>
- ![POST_in_breed](scrinshots/POST_in_breed.png) <br>
- ##### GET, PUT, DELETE to /api/breeds/<id>
- ![GET_in_breed_detail](scrinshots/GET_in_breed_detail.png) <br>
- ![PUT_in_breed_detail](scrinshots/PUT_in_breed_detail.png) <br>
- ![DELETE_in_breed_detail](scrinshots/DELETE_in_breed_detail.png) <br>







