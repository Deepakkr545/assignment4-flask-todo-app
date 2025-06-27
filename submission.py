@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']
    db.collection.insert_one({'name': itemName, 'description': itemDescription})
    return "Item added!"
