import React from 'react'
import Display from '../components/Display'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'
import About from '../components/About'
import Services from '../components/Services'

const index = () => {
  return (
    <>
    <div className="h-max bg-gradient-to-r from-sky-500 to-indigo-500 overflow-x-hidden">
      <Navbar />
      <Display />
      <About />
      <Services />
      <Footer />
    </div>
    </>
  )
}

export default index