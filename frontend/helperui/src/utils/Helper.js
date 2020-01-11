
export default class Helper{
    static getset(thisObj, stateName) {
        let capName = stateName.replace(stateName[0],stateName[0].toUpperCase());
        thisObj["get" + capName] = () => {
            return thisObj.state[stateName];
        };
        thisObj["set" + capName] = (value) => {
            let updateState = {};
            updateState[stateName] = value;
            thisObj.setState(updateState);
        };
    };
}