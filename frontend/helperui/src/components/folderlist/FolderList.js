import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/Inbox';
import Helper from '../../utils/Helper';
import CoreApi from '../../utils/CoreApi';
import './FolderList.css';


export default class FolderList extends React.Component {

  constructor(props){
    super(props);
    Helper.getset(this, "selectedIndex");
    Helper.getset(this, "filetree");
    this.state = {
      selectedIndex: "",
      filetree:{},
    };
  }

  componentDidMount(){
    this.timerId = setInterval(
      () => {
        CoreApi.filetree_get().then(
          (resp) => {
            this.setFiletree(resp.data['filetree']);
          }
        );
      }, 2000
    )
  }

  componentWillUnmount(){
    clearInterval(this.timerId);
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
          {
            (() => {
              let lists = [];
              let dirs = this.getFiletree()['dirs'];
              for(let key in dirs){
                lists.push(
                  <ListItem
                    button
                    key={key}
                    selected={getSelectedIndex() === key}
                    onClick={event => handleListItemClick(event, key)}
                  >
                    <ListItemIcon>
                      <InboxIcon />
                    </ListItemIcon>
                    <ListItemText primary={key} />
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
