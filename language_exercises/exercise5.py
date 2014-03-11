import json
status = {
	"LAB1": "Ok",
	"LAB2": "Down",
	"LAB3": "Ok"
}
convert = json.loads(status)

print convert 
