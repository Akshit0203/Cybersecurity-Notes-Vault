## General Context

- Focus was on key AI domains: language, audio/speech, and vision
    
- Covered both traditional and generative AI tasks in each domain
    
- Discussion included how data is represented and processed for each AI type
    
- Mentioned common deep learning architectures for each domain
    

## Language AI Tasks

- Two main types: text-related and generative AI
    
    - Text-related: input is text, output varies by task
        
        - Examples: language detection, entity extraction, key phrase extraction, translation
            
    - Generative AI: model generates new text
        
        - Examples: story/poem creation, summarization, Q&A (e.g., ChatGPT)
            
- Text data is sequential, made up of sentences and words
    
    - Words converted to numbers via tokenization
        
    - Sentences padded to equal length for model input
        
    - Similarity between words/sentences measured (dot/cosine similarity)
        
    - Embeddings used to represent similarity in vector space
        
- Language AI models trained on large text datasets for NLP tasks
    
    - Input/output depends on the specific task
        
    - Common architectures:
        
        - Recurrent Neural Networks (RNNs): process sequential data, store hidden states
            
        - Long Short-Term Memory (LSTM): sequential, better context retention via gates
            
        - Transformers: process in parallel, use self-attention for context
            

## Audio and Speech AI Tasks

- Two main types: audio-related and generative AI
    
    - Audio-related: input is audio/speech, output varies
        
        - Examples: speech-to-text, speaker recognition, voice conversion
            
    - Generative AI: model generates new audio
        
        - Examples: music composition, speech synthesis
            
- Audio data digitized as time-based snapshots (samples)
    
    - Standard sampling rate: 44.1 kHz (audio CDs)
        
    - Bit depth: number of bits per sample, affects information richness
        
    - Single audio sample not meaningful—need multiple samples for context
        
- Audio/speech AI models process and understand spoken language
    
    - Common architectures:
        
        - RNNs, LSTMs, Transformers
            
        - Variational Autoencoders
            
        - Waveform models
            
        - Siamese networks
            
    - All account for sequential nature of audio
        

## Vision AI Tasks

- Two main types: image-related and generative AI
    
    - Image-related: input is image, output varies
        
        - Examples: image classification, object identification, facial recognition
            
        - Used in security, biometrics, law enforcement, social media
            
    - Generative AI: model generates new images
        
        - Examples: image creation from descriptions, style transfer, high-res image generation, 3D modeling
            
- Images made up of pixels (grayscale or color)
    
    - Single pixel not meaningful—context comes from groups of pixels
        
- Vision AI models use various architectures:
    
    - Convolutional Neural Networks (CNNs): detect patterns, learn visual features
        
    - YOLO: processes image once, detects objects
        
    - Generative Adversarial Networks (GANs): generate realistic images
        

## Other AI Tasks

- Anomaly Detection: uses time series data for fraud detection, machine failure, etc.
    
- Recommendations: suggest products using data on similar products/users
    
- Forecasting: time series data for weather, stock price prediction, etc.