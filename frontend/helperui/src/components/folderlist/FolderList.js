import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import InboxIcon from '@material-ui/icons/Inbox';
import DraftsIcon from '@material-ui/icons/Drafts';
import Helper from '../../utils/Helper';
import './FolderList.css';


export default class FolderList extends React.Component {

  constructor(props){
    super(props);
    Helper.getset(this, "selectedIndex");
    this.state = {
      selectedIndex:0
    };
  }

  handleListItemClick = (event, index) => {
    this.setSelectedIndex(index);
    console.log(this.state);
  };

  render(){
    let {getSelectedIndex} = this;
    let {handleListItemClick} = this;
    return (
      <div className="folder-list">
        <List component="nav" aria-label="main mailbox folders">
          <ListItem
            button
            selected={getSelectedIndex() === 0}
            onClick={event => handleListItemClick(event, 0)}
          >
            <ListItemIcon>
              <InboxIcon />
            </ListItemIcon>
            <ListItemText primary="Inbox" />
          </ListItem>
          <ListItem
            button
            selected={getSelectedIndex() === 1}
            onClick={event => handleListItemClick(event, 1)}
          >
            <ListItemIcon>
              <DraftsIcon />
            </ListItemIcon>
            <ListItemText primary="Drafts" />
          </ListItem>
        </List>
        <Divider />
        <List component="nav" aria-label="secondary mailbox folder">
          <ListItem
            button
            selected={getSelectedIndex() === 2}
            onClick={event => handleListItemClick(event, 2)}
          >
            <ListItemText primary="Trash" />
          </ListItem>
          <ListItem
            button
            selected={getSelectedIndex() === 3}
            onClick={event => handleListItemClick(event, 3)}
          >
            <ListItemText primary="Spam" />
          </ListItem>
        </List>
      </div>
    );
  }
}
