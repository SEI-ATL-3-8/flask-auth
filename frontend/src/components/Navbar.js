import { Link } from 'react-router-dom'

const Navbar = (props) => {
  return (
    <nav>
      <Link to="/">Home</Link>
      {' | '}
      { props.user.id ?
        <>
          <span onClick={() => {
            localStorage.removeItem('userId')
            props.setUser({})
          }}>Logout</span>
          {' | '}
          <Link to="/profile">Profile</Link>
        </>
      :
        <>
          <Link to="/signup">Signup</Link>
          {' | '}
          <Link to="/login">Login</Link>
        </>
      }
    </nav>
  )
}

export default Navbar