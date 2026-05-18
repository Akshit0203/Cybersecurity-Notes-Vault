## General Context

- Demonstration of an AI visual and text analysis service
    
- Covered features: image classification, object detection, text detection, document AI, text analysis, and translation
    
- Walkthrough involved uploading various images and documents to showcase capabilities
    

## Image Classification Demo

- Uploaded local images for analysis
    
- Service assigned multiple labels to each image with confidence scores
    
    - Example: Vegetation detected with 99.23% confidence
        
    - Zebra image: Detected labels included zebra, vegetation, grassland, plant, animal
        
    - Two zebras: Detected zebra, animal, vegetation, sky, mammal
        

## Object Detection Demo

- Used an image of traffic for object detection
    
    - Service drew bounding boxes around detected objects
        
    - Detected multiple cars, taxis, and people
        
- Basket of fruit image: Detected oranges, bananas, apples, and even the bowl
    

## Text Detection Demo

- Uploaded an image of a bus with lots of text
    
    - Service extracted all visible text, including number plate "M32 hob" and number "45"
        
    - Detected both large and small text blocks
        
- Tested with image containing text in various fonts
    
    - Service extracted text line by line, recognizing different font styles
        

## Document AI / Document Understanding

- Noted that Document AI has moved to a separate service called Document Understanding
    
    - Features remain the same between both services
        
- Uploaded a receipt for analysis
    
    - Extracted all raw text from the receipt
        
    - Identified key-value pairs: transaction date, time, subtotal, tax, total
        
    - Extracted tables, including fields like patient code, terminal ID, and amount
        

## Text Analysis Features

- Applied pre-trained models to analyze a block of text
    
    - Detected language (English)
        
    - Classified paragraph as science/technology or computer-related
        
    - Extracted entities (food, computers, manual instruments) and tagged them (product, event, category)
        
    - Provided confidence scores for each entity
        
    - Extracted key phrases (e.g., food, service, early computers)
        
    - Detected sentiment (positive/negative) at both paragraph and sentence level
        
    - Identified personal identifiable information (e.g., World War II, dates) as potentially sensitive
        

## Text Translation

- Demonstrated text translation feature
    
    - Source language: English
        
    - Target language: Japanese
        
    - Successfully translated text to Japanese
        

## Custom Model Training

- Service allows training of custom models with user-provided data