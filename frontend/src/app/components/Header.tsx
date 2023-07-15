import React, { FC } from "react";

interface IProps {}

const Header: FC<IProps> = (props) => {
  return (
    <div className="flex flex-row items-center space-x-5">
      <h1 className="text-blue-500 font-bold">Nabil</h1>
      <h1>GAYL</h1>
    </div>
  );
};

export default Header;
