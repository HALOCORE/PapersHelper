import React from 'react';
import './App.css';
import Button from '@material-ui/core/Button';
import FolderList from './components/folderlist/FolderList.js';

function App() {
  return (
    <div className="app-root">
      <FolderList></FolderList>
      <Button variant="contained" color="primary">
        你好，世界
      </Button>
    </div>
  );
}

export default App;
