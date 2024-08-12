import {Link} from 'react-router-dom';

const PageNotFound = () => {
  return (
    <div>
      <h1>404</h1>
      <p>This page does not exist</p>
      <Link to="/">Go back to the homepage</Link>
    </div>
  );
}

export default PageNotFound;