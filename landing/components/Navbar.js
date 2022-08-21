import React from 'react'

const Navbar = () => {
  return (
    <>
    <nav className="bg-white border-gray-200 px-2 sm:px-4 py-5 dark:bg-gray-900">
        <div className="container flex flex-wrap justify-between items-center mx-8">
            <a href="https://github.com/Nicholas-Sidharta12365/HT6ix-2022" className="flex items-center">
                <img src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/62595384e89d1d54d704ece7_3437c10597c1526c3dbd98c737c2bcae.svg" width={32} height={32}/>
                <span className="self-center text-medium md:text-xl font-semibold whitespace-nowrap dark:text-white ml-4">IntelliCord: Meet the new Mental Health Technology</span>
            </a>
            <div className="hidden w-full md:block md:w-auto" id="navbar-default">
            </div>
        </div>
    </nav>
    </>
  )
}

export default Navbar