import React from 'react';
import { List, Avatar } from 'antd';

// const data = [
//   {
//     title: 'Ant Design Title 1',
//   },
//   {
//     title: 'Ant Design Title 2',
//   },
//   {
//     title: 'Ant Design Title 3',
//   },
//   {
//     title: 'Ant Design Title 4',
//   },
// ];

const Forum = (props) => {
  return (
    <List
    itemLayout="horizontal"
    dataSource={props.data}
    renderItem={item => (
      <List.Item>
        <List.Item.Meta
          avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
          title={<a href="https://ant.design">{item.name}</a>}
          description={item.description}
        />
      </List.Item>
    )}
    />
  );
}

export default Forum;