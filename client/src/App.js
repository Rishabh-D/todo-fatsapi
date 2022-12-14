import React, { useState, useEffect } from 'react';
import './App.css';
import TodoView from './components/TodoListView';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {

  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')



  // Read all todos
  useEffect(() => {
    axios.get('https://3wbnqk4oib.execute-api.ap-south-1.amazonaws.com/dev/api/todo/', {
    })
      .then(res => {
        setTodoList(res.data)
      })
  });

  // Post a todo
  const addTodoHandler = () => {
    axios.post('https://3wbnqk4oib.execute-api.ap-south-1.amazonaws.com/dev/api/todo/', { 'title': title, 'description': desc })
      .then(res => console.log(res))
    setTitle(prev => '')
    setDesc(prev => '')
    console.log(desc, title)
  };

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px" }} >
      <h1 className="card text-white bg-primary mb-1">Task Manager</h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6>
      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
        <span className="card-text">
          <input className="mb-2 form-control titleIn" onChange={e => setTitle(e.target.value)} placeholder='Title' />
          <input className="mb-2 form-control desIn" onChange={e => setDesc(e.target.value)} placeholder='Description' />
          <button className="btn btn-outline-primary mx-2 mb-3" style={{ 'borderRadius': '50px', "fontWeight": "bold" }} onClick={addTodoHandler}>Add Task</button>
        </span>
        <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
        <div >
          {todoList.length > 0 ? <TodoView todoList={todoList} /> : null}
        </div>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0" >Copyright 2022, All rights reserved &copy;</h6>
    </div>
  );
}

export default App;