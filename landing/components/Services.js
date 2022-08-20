import React, { useState } from 'react'

const Services = () => {
    const [youtubeID] = useState('SPTfmiYiuok')

  return (
    <>
    <div className='font-bold text-4xl text-center my-16'>
        Our Services
    </div>
    <div className='grid lg:grid-cols-2 mx-16 mb-16 lg:h-96 gap-6'>
        <div className='font-semibold text-2xl'> We provide a free usable Discord Bot that tracks each of the user's past 2 hours of message/chat and analyze it using our model that we have trained using co:here and create a solution/generate motivation for the user based on the result of the model. Here we have the demo video of our project.</div>
        <div className=''>
            <iframe className='video h-full w-full'
                title='Youtube player'
                sandbox='allow-same-origin allow-forms allow-popups allow-scripts allow-presentation'
                src={`https://youtube.com/embed/${youtubeID}?autoplay=0`}>
            </iframe>
        </div>
    </div>
    </>
  )
}

export default Services