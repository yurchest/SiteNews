import React from 'react';
import { useRef } from 'react';
import {FaBars, FaTimes} from "react-icons/fa"
import "./Navbar.css"

const Navbar = () => {

    const navRef = useRef();

    const showNavbar = () => {
        console.log("aaa")
        navRef.current.classList.toggle("responsive_nav");
    }

    return (
        <header>
            <h3>Logo</h3>
            <nav ref = {navRef}>   
                <a href="/home">Home</a>
                <a href="/#">Str1</a>
                <a href="/#">Str2</a>
                <a href="/#">Str3</a>
                <button 
                    className='nav-btn nav-close-btn' 
                    onClick ={showNavbar}>   
                    <FaTimes/>
                </button>
            </nav>
            <button className='nav-btn' onClick = {showNavbar}>
                <FaBars/>
            </button>   

            
        </header>
    );
};

export default Navbar;