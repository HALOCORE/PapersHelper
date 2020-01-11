import React from 'react';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Helper from '../../utils/Helper';
import CoreApi from '../../utils/CoreApi';
import './PaperInfo.css';


export default class PaperInfo extends React.Component {

  constructor(props) {
    super(props);
    Helper.getset(this, "fileid");
    Helper.getset(this, "fileSummary");
    Helper.getset(this, "fileRefs");
    this.state = {
      fileid: "",
      fileSummary: {},
      fileRefs: {}
    };
  }

  infoUpdate = () => {
    let {fileid} = this.props;
    CoreApi.file_summary_get(fileid).then(
      (resp) => {
        this.setFileSummary(resp.data['summary']);
      }
    );
    CoreApi.file_refs_get(fileid).then(
      (resp) => {
        this.setFileRefs(resp.data['refs']);
      }
    )
  }

  componentDidMount() {
    this.infoUpdate();
  }

  render() {
    let {fileSummary, fileRefs} = this.state;
    return (
      <div className="paper-info">
      <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography>{JSON.stringify(fileSummary)}</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography>
            {JSON.stringify(fileRefs)}
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      </div>
    );
  }
}
