import React from "react"

const Display = () => {
  return (
    <>
    <div className="grid xl:grid-cols-2 my-16 mx-8 grid-cols-1">
        <img src="https://bgsbali.com/wp-content/uploads/2022/02/Blog-56.jpg" alt="" className="border rounded"/>
        <div className="mx-8 mt-12">
            <div className="text-5xl font-bold">Check up on your mental health on your daily online journey</div>
            <div className="my-8 text-2xl">Join us and let's conquer our mental health challenges together</div>
            <a href="https://github.com/Nicholas-Sidharta12365/HT6ix-2022" className="">
                <button class="bg-white hover:bg-gray-100 text-gray-800 font-bold text-xl py-2 px-4 border border-gray-400 rounded shadow">
                    Join Now
                </button>
            </a>
        </div>
    </div>
    </>
  )
}

export default Display