import React from "react";

const Home = () => {
  return (
    <>
      <h5>Banner</h5>

      <div className="products-heading">
        <h2>Best Selling Products</h2>
        <p>Speaker of many variations</p>
      </div>
      <div className="products-container">
        {["product 01", "product 02"].map((product) => {
          return <p>{product}</p>;
        })}
      </div>

      <footer>this is footer</footer>
    </>
  );
};

export default Home;
