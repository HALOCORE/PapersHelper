import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import PageIcon from '@material-ui/icons/Pages';
import Helper from '../../utils/Helper';
import CoreApi from '../../utils/CoreApi';
import './PaperList.css';
import PaperInfo from '../paperinfo/PaperInfo';


export default class PaperList extends React.Component {

  constructor(props) {
    super(props);
    Helper.getset(this, "selectedIndex");
    Helper.getset(this, "files");
    this.state = {
      selectedIndex: "",
      files: [],
    };
  }

  listUpdate = () => {
    CoreApi.file_search().then(
      (resp) => {
        this.setFiles(resp.data['files']);
      }
    );
  }

  componentDidMount() {
    this.listUpdate();
  }

  handleListItemClick = (event, index) => {
    this.setSelectedIndex(index);
    console.log(this.state);
  };

  render() {
    let { getSelectedIndex } = this;
    let { handleListItemClick } = this;
    return (
      <div className="paper-list">
        <List component="nav" aria-label="main mailbox folders">
          {
            (() => {
              let lists = [];
              let files = this.getFiles();
              for (let i = 0; i < files.length; i++) {
                let file = files[i];
                lists.push(
                  <ListItem
                    button
                    key={file}
                    selected={getSelectedIndex() === file}
                    onClick={event => handleListItemClick(event, file)}
                  >
                    <ListItemIcon>
                      <PageIcon />
                    </ListItemIcon>
                    <ListItemText primary={file}
                    secondary={
                      <React.Fragment>
                        <PaperInfo fileid={file}/>
                      </React.Fragment> 
                    }/>
                  </ListItem>
                )
              };
              return lists;
            })()
          }

        </List>
      </div>
    );
  }
}
