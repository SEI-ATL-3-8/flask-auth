import { useState, useEffect } from 'react'
import { Route, Redirect } from 'react-router-dom'
import axios from 'axios'
import './App.css';

import Navbar from './components/Navbar'
import Home from './pages/Home'
import Signup from './pages/Signup'
import Login from './pages/Login'
import Profile from './pages/Profile'

function App() {
  const [user, setUser] = useState({})

  const fetchUser = () => {
    if (localStorage.getItem('userId')) {
      axios.get(`${process.env.REACT_APP_BACKEND_URL}/users/verify`, {
        headers: {
          Authorization: localStorage.getItem('userId')
        }
      })
      .then((response) => {
        setUser(response.data.user)
      })
    }
  }
  useEffect(fetchUser, [])
  
  return (
    <div>
      <Navbar user={user} setUser={setUser} />

      <Route path="/" exact component={Home} />

      <Route path="/signup" render={(routeInfo) => {
        if (user.id) {
          return <Redirect to="/profile" />
        } else {
          return <Signup setUser={setUser} />
        }
      }} />

      <Route path="/login" render={(routeInfo) => {
        if (user.id) {
          return <Redirect to="/profile" />
        } else {
          return <Login setUser={setUser} />
        }
      }} />
      
      <Route path="/profile" render={(routeInfo) => {
        if (user.id) {
          return <Profile user={user} />
        } else {
          return <Redirect to="/login" />
        }
      }} />
    </div>
  );
}

export default App;
