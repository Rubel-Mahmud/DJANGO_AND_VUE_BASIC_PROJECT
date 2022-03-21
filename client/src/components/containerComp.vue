<template>
  <div class="row">
    <div class="col-md-5">
      <input v-model="url" type="hidden" class="form-control mt-2" placeholder="Url"/>
      <input v-model="title" type="text" class="form-control mt-2" placeholder="Title"/>
      <input v-model="body" type="text" class="form-control mt-2" placeholder="Body"/>
      <button class="btn btn-success form-control mt-2" @click="postBlog">Save</button>
    </div>
    <div class="col-md-7">
      <table class="table mt-2">
        <thead>
          <th>Url</th>
          <th>Title</th>
          <th>Body</th>
          <th>Edit</th>
          <th>Delete</th>
        </thead>
        <tbody>
          <tr v-for="blog in blogs" :key="blog.url">
            <td>{{blog.url}}</td>
            <td>{{blog.title}}</td>
            <td>{{blog.body}}</td>
            <td>
              <button class="btn btn-sm btn-success" @click="getOne(blog)">
                <i class="fa-solid fa-pencil"></i>
              </button>
            </td>
            <td>
              <button class="btn btn-sm btn-success" @click="deleteOne(blog.url)">
                <i class="fa-solid fa-trash"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'containerComp',
  props: {
    msg: String
  },
  data(){
    return{
      blogs : null,
      url : '',
      title : '',
      body : ''
    }
  },
  mounted(){
    this.getAll()
  },
  methods : {
    getAll(){
      axios.get(`http://127.0.0.1:8000/bloggers/`)
      .then((res)=>{
        this.blogs = res.data;
        this.url = '',
        this.title = '',
        this.body = ''
      })
    },
    
    getOne(blog){
      this.url = blog.url,
      this.title = blog.title,
      this.body = blog.body
    },
    
    deleteOne(url){
      axios.delete(url, {
        auth : {
          username : 'rubel',
          password : 'r'
        }
      })
      .then(()=>{
        this.getAll();
        console.log('Deleted this item..');
      })
    },
    
    postBlog(){
      if(this.url == ''){
        axios.post(`http://127.0.0.1:8000/bloggers/`, 
        {title:this.title, body:this.body}, 
        {auth:{username:'rubel',password:'r'}})
        .then(()=>{
          this.getAll();
        })
      }
      else{
        axios.put(this.url, 
        {title:this.title, body:this.body}, 
        {auth:{username:'rubel',password:'r'}})
        .then(()=>{
          this.getAll();
        })
      }
    }

  }
}
</script>

<style>
#brandName{
  font-family: 'Dancing Script', cursive;
  color:#fff;
}

.myNav ul li a{
  color:#fff !important;
  padding-right:15px;
  text-decoration: none;
}
</style>
