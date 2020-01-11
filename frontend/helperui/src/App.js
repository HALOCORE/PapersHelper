import React from 'react';
import './App.css';
import Button from '@material-ui/core/Button';
import FolderList from './components/folderlist/FolderList';
import PaperList from './components/paperlist/PaperList';
import CoreApi from './utils/CoreApi';


function App() {
  let reloader = () => {
    CoreApi.reloads().then(() => console.log("Reload Succeed."));
  };
  return (
    <div className="app-root">
      <div>
        <Button onClick={reloader} variant="contained" color="primary">
        Reload
        </Button>
      </div>
      <div>
        <FolderList/>
        <PaperList/>
      </div>
    </div>
  );
}

export default App;
