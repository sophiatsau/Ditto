import './LandingPage.css'



const LandingPage = () => {
    return (
      <div>
        <section className="hero">
          <h1>Welcome to Ditto</h1>
          <p>Learn English with our program for second-generation learners.</p>
          <a href="#features" className="cta-button">Learn More</a>
        </section>

        <section id="features" className="features">
          <h2>Features</h2>
          <div className="feature">
            <h3>Practice With Our Ai ChatBot!</h3>
            <p>Speak with our AI chatbot that taylors conversations to real life situations!</p>
          </div>
          <div className="feature">
            <h3>Phrase of the day!</h3>
            <p>Learn a daily phrase that applies to real life situations!</p>
          </div>
        </section>

        <section id="testimonials" className="testimonials">
          <h2>What Our Students Say</h2>
          <div className="testimonial">
            <p>&quot;Ditto has transformed my English learning experience. The lessons are fun and engaging!&quot; - Justin</p>
            <div className="profile">
              <img src="https://i.postimg.cc/tJgwPHNk/IMG-0074.jpg" alt="Profile of Justin" />
            </div>
          </div>
        </section>

        <footer id="contact" className="footer">
          <p>Contact us at Student@appacademy.com</p>
        </footer>
      </div>
    );
  };

  export default LandingPage;
