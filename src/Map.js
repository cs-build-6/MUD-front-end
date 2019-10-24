import React, { useState, useEffect } from "react";
import axiosWithAuth from "./auth/axiosAuth";

/**
 * def heroku_query(query): # A simple function to use requests.post to make the API call. 
    

    
    request = requests.post('https://danpatadv.herokuapp.com/graphql/', json={'query': query})
    if get.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
all_rooms_query = { rooms { id x y floor nTo sTo eTo wTo uTo dTo region description itemdesc} }
**/    


function Map({ currentRoom }) {
  const [rooms, setRooms] = useState([]);
  useEffect(() => {
    axiosWithAuth()
      .get("https://danpatadv.herokuapp.com/graphql/")

      .then(res => {
        setRooms(res.data);
      })
      .catch(error => {
        console.log(error.message);
      });
  }, []);
  return (
    <>
      <div
        className="map-container"
        style={{
          position: "relative",
          width: "170px",
          height: "200px",
          margin: "0 auto"
        }}
      >
        {rooms.map(item => {
          let roomNumber = item.title.split(" ");
          let { x, y } = item;
          x *= 30;
          y *= 30;
          let styles;
          if (item.title === currentRoom) {
            styles = {
              position: "absolute",
              bottom: y,
              left: x,
              width: "20px",
              height: "20px",
              background: "red",
              borderRadius: "100%"
            };
          } else {
            styles = {
              position: "absolute",
              bottom: y,
              left: x,
              width: "20px",
              height: "20px",
              background: "yellow",
              borderRadius: "100%"
            };
          }

          return (
            <div key={item.title} style={styles} name={item.room}>
              {roomNumber[1]}
            </div>
          );
        })}
      </div>
    </>
  );
}
export default Map;
