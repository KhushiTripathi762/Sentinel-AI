@router.post("/prompt")
def check_prompt(request: PromptRequest):

    logger.info("Prompt analysis request received")

    if not request.text or not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty or only spaces."
        )

    try:
        result = detect_prompt(request.text)
        logger.info(f"Result: {result}")
        return result

    except Exception as e:
        logger.exception("Prompt detection failed")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )