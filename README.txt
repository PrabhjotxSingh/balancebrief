//Running back end
pip install uvicorn
pip install fastapi
//Might need to do this next bit if on windows
pip install fastapi[all]
//cd into api folder
python -m uvicorn main:app --reload

//Running front end
//cd in bb.ui folder
npm install
ng serve