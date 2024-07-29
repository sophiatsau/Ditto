import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <header>
      <nav className="navbar">
        <div className="logo">Ditto</div>
        <ul className="nav-links">
          <li>
            <NavLink to="/">Home</NavLink>
          </li>
          <li>
            <NavLink to="#features">Features</NavLink>
          </li>
          <li>
            <NavLink to="#contact">Contact</NavLink>
          </li>
          <li>
            <ProfileButton />
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Navigation;
