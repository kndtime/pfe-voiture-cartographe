import React, { Component } from 'react';
import PropTypes from "prop-types";
// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import BugReport from "@material-ui/icons/BugReport";
import Code from "@material-ui/icons/Code";
import Cloud from "@material-ui/icons/Cloud";

// core components
import Danger from "components/Typography/Danger.jsx";
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import RosLib from 'roslib'

import logo from './logo.svg';
import "assets/css/material-dashboard-react.css?v=1.5.0";
import dashboardStyle from "assets/jss/views/dashboardStyle.jsx";

class App extends React.Component {
  constructor(props) {
    super(props);
    let ros;
    let listener;
    this.state = {
      mobileOpen: false,
      value: 0,
      cpu: {
        percent: 0.0
      },
      ram: {
        percent: 0.0,
        total: 0,
        used: 0,
        free: 0
      },
      disk: {
        total: 0,
        used: 0,
        free: 0,
        percent: 0,
        read_bytes_sec: 0,
        write_bytes_sec: 0
      },
      io: {
        sent_bytes_sec: 0,
        received_bytes_sec: 0
      },
      gyro: {
        x: 0.0,
        y: 0.0,
        z: 0.0
      },
      gps: {
        lat: 0.0,
        lng: 0.0
      }
    };
    this.resizeFunction = this.resizeFunction.bind(this);
  }

  componentDidMount() {
    window.addEventListener("resize", this.resizeFunction);
    if (!ros)
      var ros = new RosLib.Ros({url : 'ws://localhost:11311'});

    ros.on('connection', function() {
      console.log('Connected to websocket server.');
    });

    ros.on('error', function(error) {
      console.log('Error connecting to websocket server: ', error);
    });

    ros.on('close', function() {
      console.log('Connection to websocket server closed.');
    });

    var listener = new RosLib.Topic({
      ros : ros,
      name : '/Buggy/buggyServer',
      messageType : 'std_msgs/String'
    });

    // Then we add a callback to be called every time a message is published on this topic.
    listener.subscribe(function(message) {
      console.log('Received message on ' + listener.name + ': ' + message.data);
      // If desired, we can unsubscribe from the topic as well.
    });
  }

  resizeFunction() {
    if (window.innerWidth >= 960) {
      this.setState({ mobileOpen: false });
    }
  }
  componentWillUnmount() {
    window.removeEventListener("resize", this.resizeFunction);
    if (!this.listener)
      this.listener.unsubscribe()
  }
  render() {
    const { classes, ...rest } = this.props;
    return (
      <div className={classes.wrapper}>
        <GridContainer>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="warning" stats icon>
                <CardIcon color="warning">
                  <AccessTime>content_copy</AccessTime>
                </CardIcon>
                <p className={classes.cardCategory}>Carte SD</p>
                <h3 className={classes.cardTitle}>
                  {this.state.disk.free} / {this.state.disk.total} <small>GB</small>
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                  <Danger>
                    <Warning />
                  </Danger>
                  <a href="#pablo" onClick={e => e.preventDefault()}>
                    Get more space
                  </a>
                </div>
              </CardFooter>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="success" stats icon>
                <CardIcon color="success">
                  <Store />
                </CardIcon>
                <p className={classes.cardCategory}>CPU</p>
                <h3 className={classes.cardTitle}>{this.state.cpu.percent} <small>%</small></h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                  <DateRange />
                  Last 24 Hours
                </div>
              </CardFooter>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="danger" stats icon>
                <CardIcon color="danger">
                  <Code>info_outline</Code>
                </CardIcon>
                <p className={classes.cardCategory}>Connection plateforme</p>
                <h3 className={classes.cardTitle}><small>Faible</small></h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                  <LocalOffer />
                  Connecté
                </div>
              </CardFooter>
            </Card>
          </GridItem>
        </GridContainer>
      </div>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(dashboardStyle)(App);
